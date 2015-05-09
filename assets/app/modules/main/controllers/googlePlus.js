"use strict";

angular.module('app.main').controller('googlePlusController', function ($scope, $http, googlePlusService) {

     var googlePlusUserID = window.googlePlusUserID;

    // The whole profile
    $scope.profile = googlePlusService.profile || googlePlusService.getProfile(googlePlusUserID);

    // About me to be rendered via service
    $scope.getAboutMe = googlePlusService.getAboutMe;

    // Image to be resized via service
    $scope.getProfileImageUrl = googlePlusService.getProfileImageUrl;

    // Check if it's ready (used to show/hide the html)
    $scope.isProfileReady = function (){
        return !angular.equals({}, $scope.profile);
    };

});