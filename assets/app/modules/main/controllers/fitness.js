"use strict";

angular.module('app.main').controller('fitnessController', function ($scope, $http, fitnessService) {

    var runkeeperUserID = window.runkeeperUserID;

    // Weight
    $scope.weightMeasurements = fitnessService.getWeightMeasurements(runkeeperUserID);

    // Latest Activity
    $scope.latestActivity = fitnessService.getLatestActivity(runkeeperUserID);

    // Activities Records
    $scope.records = fitnessService.getActivityRecords(runkeeperUserID);

    // @todo Should it just check one?
    $scope.isFitnessDataReady = function () {
        return !angular.equals({}, $scope.weightMeasurements) && !angular.equals({}, $scope.getLatestActivity) && !angular.equals({}, $scope.getLatestActivity);
    };

});