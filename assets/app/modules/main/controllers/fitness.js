"use strict";

angular.module('app.main').controller('fitnessController', function($scope, $http) {

    // Stub here to get my personal data
    var userId = '29509824';

    $scope.metrics = [];

    // @todo check if this should be a resource and moved to service and promise

    // Get some weight
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

    // Get latest activity
    $http.get('/metrics/runkeeper/' + userId + '/fitness_activities')
        .success(function (data, status, headers, config) {
            // get the 1st
            // @todo move these elsewhere
            // Get latest activity
            $http.get('/metrics/runkeeper/' + userId + data.items[0].uri)
                .success(function (data, status, headers, config) {
                    $scope.metrics.push({
                        'Latest Activity': data.type,
                        'Latest Activity Distance': Math.round(data.total_distance/1000) + 'Km',
                        'Latest Activity Start Time': data.start_time,
                        'Latest Activity Calories': data.total_calories + 'Kcal',
                        'Latest Activity Duration': Math.round(data.duration/60) + 'sec'
                    });
                })
                .error(function (data, status, headers, config) {
                    // log error
                });

        })
        .error(function (data, status, headers, config) {
            // log error
        });


});