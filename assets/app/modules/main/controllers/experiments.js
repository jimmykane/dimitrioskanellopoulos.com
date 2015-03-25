"use strict";

angular.module('app.main').controller('experimentsController', function($scope, $http) {

    // @todo check if this should be a resource
    $http.get('/assets/app/data/experiments.json')
        .success(function(data, status, headers, config) {
            $scope.links = data;
        })
        .error(function(data, status, headers, config) {
            // log error
        });
});