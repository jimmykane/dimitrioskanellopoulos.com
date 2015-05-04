"use strict";

angular.module('app.main').controller('mainController', function ($scope, googlePlusService) {

    var googlePlusUserID = window.googlePlusUserID;

    // Profile
    $scope.googlePlusProfile = googlePlusService.getProfile(googlePlusUserID);

});