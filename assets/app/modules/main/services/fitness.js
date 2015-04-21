"use strict";


//@todo Check it this belongs to this main modules
angular.module('app.main').factory('fitnessService', function ($http, $q) {

    var fitnessService = {};

    // @todo combine calls to one
    fitnessService.getUserRunkeeperMetrics = function (userId, call) {
        var deffered = $q.defer();
        // Get some weight
        $http.get('/metrics/runkeeper/' + userId + '/' + call)
            .success(function (data, status, headers, config) {
                if (status !== 200) {
                    deffered.resolve(data.status);
                    return;
                }
                // Extend with new data
                angular.extend(fitnessService[call], data);
                deffered.resolve(status);
            })
            .error(function (data, status, headers, config) {
                deffered.reject(status);
                console.log(data, status, headers, config);
            });
        return deffered.promise;
    };

    fitnessService.getWeightMeasurements = function (userId) {
        fitnessService.getWeightMeasurements = fitnessService.getWeightMeasurements || {};
        fitnessService.getUserRunkeeperMetrics(userId, 'getWeightMeasurements');
        return fitnessService.getWeightMeasurements;
    };

    fitnessService.getLatestActivity = function (userId) {
        fitnessService.latestActivity = fitnessService.latestActivity || {};
        fitnessService.getUserRunkeeperMetrics(userId, 'latestActivity');
        return fitnessService.latestActivity;
    };

    fitnessService.getActivityRecords = function (userId) {
        fitnessService.records = fitnessService.records || {};
        fitnessService.getUserRunkeeperMetrics(userId, 'records');
        return fitnessService.records;
    };

    return fitnessService;

});