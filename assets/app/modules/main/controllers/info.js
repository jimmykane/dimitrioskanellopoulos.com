"use strict";

angular.module('app.main').controller('infoController', function($scope, $http) {

    // Query here because its an array and get expects an object
    $http.get('/assets/app/data/info.json')
        .success(function(data, status, headers, config) {
            $scope.links = data;
        })
        .error(function(data, status, headers, config) {
            // log error
        });
});