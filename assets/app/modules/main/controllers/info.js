"use strict";

angular.module('app.main').controller('infoController', function($scope, jsonService) {

    // Query here because its an array and get expects an object
    jsonService.query(function(data){
        $scope.data = data;
    });

});