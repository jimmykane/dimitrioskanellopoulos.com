"use strict";

angular.module('app.main').controller('socialLinksController', function ($scope, $http, googlePlusService) {

    var googlePlusUserID = window.googlePlusUserID;

    // Profile
    $scope.profile = googlePlusService.getProfile(googlePlusUserID);

});