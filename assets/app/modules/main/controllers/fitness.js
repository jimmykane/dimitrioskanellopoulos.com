"use strict";

angular.module('app.main').controller('fitnessController', function($scope, $http) {

    // Stub here to get my personal data
    var userId = '29509824';

    $scope.metrics = [];

    // @todo check if this should be a resource and moved to service and promise

    // Get some
    $http.get('/metrics/runkeeper/' + userId + '/weight')
        .success(function(data, status, headers, config) {
            debugger;
            // Get the 1st one
            $scope.metrics.push({Weight: data.items[0].weight});
        })
        .error(function(data, status, headers, config) {
            // log error
        });

});