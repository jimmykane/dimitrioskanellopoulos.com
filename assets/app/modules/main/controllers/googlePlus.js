"use strict";

angular.module('app.main').controller('googlePlusController', function ($scope, $http, googlePlusService) {

     var googlePlusUserID = window.googlePlusUserID;

    // The whole profile
    $scope.googlePlusProfile = googlePlusService.getProfile(googlePlusUserID);

    // About me to be rendered via service
    $scope.getAboutMe = googlePlusService.getAboutMe;

    // Image to be resized via service
    $scope.getProfileImageUrl = googlePlusService.getProfileImageUrl;

});