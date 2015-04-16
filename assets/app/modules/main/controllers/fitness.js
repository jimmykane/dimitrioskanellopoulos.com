"use strict";

angular.module('app.main').controller('fitnessController', function($scope, $http) {

    // Stub here to get my personal data
    var userId = '29509824';

    // @todo check if this should be a resource


    // Get some
    $http.get('/metrics/runkeeper/' + userId + '/records')
        .success(function(data, status, headers, config) {
            debugger;
            $scope.metrics = data;
        })
        .error(function(data, status, headers, config) {
            // log error
        });
});