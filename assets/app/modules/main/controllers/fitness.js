"use strict";

angular.module('app.main').controller('fitnessController', function ($scope, $http, fitnessService) {

    // Stub here to get my personal data
    var userId = '29509824';
    $scope.metrics = [];

    // Weight
    $scope.weightMeasurements = fitnessService.getWeightMeasurements(userId);

    // Latest Activity
    $scope.latestActivity = fitnessService.getLatestActivity(userId);

    // Activities Records
    $scope.records = fitnessService.getActivityRecords(userId);

});