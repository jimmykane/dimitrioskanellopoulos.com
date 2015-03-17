"use strict";

var app = angular.module(
    'app', [
        //'ngRoute',
        //'ngAnimate'
        //'mainApp.main'
    ],
    function($interpolateProvider) {
        /* INTERPOLATION
        * Normal Angular {{}} now becomes {[{}]} so take care. */
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    }
);

/**
 * Config
 */
app.config(function($locationProvider, $routeProvider) {
    /*
     * Enabled HTML5 mode. Probably will not support
     * any browser especially < IE10
     */
    $locationProvider.html5Mode(true);

    /*
     * Routes for the mainApp
     */
    $routeProvider.when('/', {
        templateUrl: '/assets/app/views/main.html',
        controller:  'appController'
    }).otherwise({redirectTo: '/404.html'}); // stub for production
});


/**
 * Controller
 */
app.controller('appController', function($scope, $location) {
    // Nothing for now. Maybe some static stuff
//    $scope.go_to_list = function(){
//        $location.path('/list/');
//    }
});