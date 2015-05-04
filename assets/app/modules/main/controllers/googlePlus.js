"use strict";

angular.module('app.main').controller('googlePlusController', function ($scope, $http, googlePlusService) {

    var googlePlusUserID = window.googlePlusUserID;

    // Profile
    $scope.profile = googlePlusService.getProfile(googlePlusUserID);

});