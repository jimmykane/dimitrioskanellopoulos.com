"use strict";

angular.module('app.main').controller('fitnessController', function($scope, $http, fitnessService) {

    // Stub here to get my personal data
    var userId = '29509824';

    $scope.metrics = [];

    // @todo check to inject weight via service

    // Get latest activity
    $http.get('/metrics/runkeeper/' + userId + '/fitnessActivities')
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
                        'Latest Activity Duration': (data.duration/60) + 'min'
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