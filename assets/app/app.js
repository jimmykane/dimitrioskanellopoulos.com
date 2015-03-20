"use strict";

var app = angular.module(
    'app', [
        'ngRoute',
        //'ngAnimate'
        'app.main'
    ]
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
        templateUrl: '/assets/app/views/modules/main.html',
        controller:  'appController'
    }).otherwise({redirectTo: '/404'});
});


/**
 * Controller
 */
app.controller('appController', function($scope, $location) {
    $scope.greeting = 'Hola!';
});