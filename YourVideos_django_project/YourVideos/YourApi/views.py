from .serializers import OurVideoSerializer, OurRatingSerilaizer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly 
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework import permissions
from django.shortcuts import render
from .models import Video, Rating
from rest_framework.authentication import TokenAuthentication



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = OurVideoSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)


    @action(detail=True)
    def rate_video(self, request, pk=None):
        if 'stars'  in request.data:
            video = Video.objects.get(id=pk)
            stars = request.data['stars']
            comments = request.data['comments']
            user = request.user

        try:
            rating = Rating.objecta.get(user = user.id, video=video.id)
            rating.stars = stars
            rating.comments = comments
            rating.save()

            serializer = OurRatingSerilaizer(rating, many=False)
            response = {'message':'rating has been updated', 'result':serializer.data}
            return response(response, status=status.HTTP_200_OK)


        except:
            rating = Rating.objects.create(user=user, video=video, stars=stars, comments=comments)

            serializer =  OurRatingSerilaizer(rating, many=False)
            response = {'message':'rating created', 'result':serializer.data}
            return response(response, status=status.HTTP_200_OK)


        else:
            response = {'message':'Please enter the stars for the rating', 'result':serializer.data}
            return response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = OurRatingSerilaizer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    authentication_classes = (TokenAuthentication,)

    def delete(self, request, *args, **kwrgs):
        response = {'message':'Rating cannot be Updateds, due to the bad request'}
        return response(response, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
