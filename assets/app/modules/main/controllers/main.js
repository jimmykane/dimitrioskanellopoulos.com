"use strict";

angular.module('app.main').controller('mainController', function ($scope, googlePlusService, $sce) {

    var googlePlusUserID = window.googlePlusUserID;

    // Profile
    $scope.googlePlusProfile = googlePlusService.getProfile(googlePlusUserID);

    $scope.getAboutMe = function (){
         return $sce.trustAsHtml($scope.googlePlusProfile.aboutMe);
    };

    $scope.getProfileImageUrl = function(){
        if (!$scope.googlePlusProfile.image){
            return;
        }
        return $scope.googlePlusProfile.image.url.slice(0, -2) + '100';
    }

});