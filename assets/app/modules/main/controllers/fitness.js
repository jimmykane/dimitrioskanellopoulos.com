"use strict";

angular.module('app.main').controller('fitnessController', function($scope, $http) {

    // Stub here to get my personal data
    var userId = '29509824';

    $scope.metrics = [];

    // @todo check if this should be a resource and moved to service and promise

    // Get some
    $http.get('/metrics/runkeeper/' + userId + '/weight')
        .success(function(data, status, headers, config) {
            // Find weight and fat percentage if possible
            var weight;
            var fatPercent;
            for (var weightMeasurement in data.items){
                if (!weight && data.items[weightMeasurement].weight){
                    weight = data.items[weightMeasurement].weight;
                }
                if (!fatPercent && data.items[weightMeasurement].fat_percent){
                    fatPercent = data.items[weightMeasurement].fat_percent;
                }
            }
            $scope.metrics.push({
                Weight: weight + 'Kg',
                'Body Fat': fatPercent + '%'
            });
        })
        .error(function(data, status, headers, config) {
            // log error
        });
});