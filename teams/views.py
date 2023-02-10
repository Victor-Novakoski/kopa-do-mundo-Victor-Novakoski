from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .models import Team
from django.forms.models import model_to_dict
from django.core.exceptions import ValidationError
from .utils import (
    NegativeTitlesError,
    validate_title,
    InvalidYearCupError,
    validate_first_cup,
    ImpossibleTitlesError,
    validate_impossible_titles,
)


# Create your views here.


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        teams_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        try:
            # validations
            validate_title(request.data["titles"])
            validate_first_cup(request.data["first_cup"])
            validate_impossible_titles(
                request.data["titles"], request.data["first_cup"]
            )

            team = Team.objects.create(**request.data)
            team_dict = model_to_dict(team)
            return Response(team_dict, status.HTTP_201_CREATED)
        except ImpossibleTitlesError as error:
            return Response({"error": f"{error}"}, status.HTTP_400_BAD_REQUEST)
        except NegativeTitlesError as error:
            return Response({"error": f"{error}"}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as error:
            return Response({"error": f"{error}"}, status.HTTP_400_BAD_REQUEST)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
