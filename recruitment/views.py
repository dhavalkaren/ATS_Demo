from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q, IntegerField, Value, When, Case
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    # Custom Search API
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"error": "Query parameter 'q' is required."}, status=400)

        query_words = query.split()
        filters = Q()
        for word in query_words:
            filters |= Q(name__icontains=word)

        candidates = Candidate.objects.filter(filters)

        match_count_expr = sum(
            Case(
                When(name__icontains=word, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            ) for word in query_words
        )

        candidates = candidates.annotate(match_count=match_count_expr)
        relevancy = candidates.order_by('-match_count')
        serializer = self.get_serializer(relevancy, many=True)
        return Response(serializer.data)
