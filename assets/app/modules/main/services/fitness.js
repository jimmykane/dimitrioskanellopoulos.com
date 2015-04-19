"use strict";


//@todo Check it this belongs to this main modules
angular.module('app.main').factory('fitnessService', function($http, $q) {

    var fitnessService = {};
    fitnessService.weightMeauremnts = {};


    fitnessService.getUserWeightMeasurements = function(user){

        // Get some weight
        $http.get('/metrics/runkeeper/' + userId + '/weight')
        .success(function(response, status, headers, config) {
            if (response.status.code !== 200){
                deffered.resolve(response.status);
                return;
            }

            var weight;
            var fatPercent;
            for (var weightMeasurement in response.items){
                if (!weight && response.items[weightMeasurement].weight){
                    weight = response.items[weightMeasurement].weight;
                }
                if (!fatPercent && response.items[weightMeasurement].fat_percent){
                    fatPercent = response.items[weightMeasurement].fat_percent;
                }
            }
            fitnessService.weightMeauremnts.weight = weight + 'Kg';
            fitnessService.weightMeauremnts.bodyFat =  fatPercent + '%';

            deffered.resolve(response.status);
        })
        .error(function(response, status, headers, config) {
            deffered.reject(response.status);
            console.log(response, status, headers, config);
        });
        return deffered.promise;
    };



    return fitnessService;

});