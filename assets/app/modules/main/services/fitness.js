"use strict";


//@todo Check it this belongs to this main modules
angular.module('app.main').factory('fitnessService', function ($http, $q) {

    var fitnessService = {};
    var weightMeasurements = {};
    var latestActivity = {};


    fitnessService.getUserWeightMeasurements = function (userId) {
        var deffered = $q.defer();
        // Get some weight
        $http.get('/metrics/runkeeper/' + userId + '/weightMeasurements')
            .success(function (data, status, headers, config) {
                debugger;

                if (status !== 200) {
                    deffered.resolve(data.status);
                    return;
                }

                weightMeasurements.weight = data['weight'] + 'Kg';
                weightMeasurements.fatPercent = data['fat_percent'] + '%';

                deffered.resolve(status);
            })
            .error(function (data, status, headers, config) {
                deffered.reject(status);
                console.log(data, status, headers, config);
            });
        return deffered.promise;
    };

    fitnessService.getUserLatestActivity = function (userId) {
        var deffered = $q.defer();
        // Get some weight
        $http.get('/metrics/runkeeper/' + userId + '/weight')
            .success(function (data, status, headers, config) {
                debugger;
                if (status !== 200) {
                    deffered.resolve(data.status);
                    return;
                }

                // Do stuff here again

                deffered.resolve(status);
            })
            .error(function (data, status, headers, config) {
                deffered.reject(status);
                console.log(data, status, headers, config);
            });
        return deffered.promise;
    };

    fitnessService.weightMeasurements = function(){
        return weightMeasurements;
    };

    fitnessService.latestActivity = function(){
        return latestActivity;
    };

    return fitnessService;

});