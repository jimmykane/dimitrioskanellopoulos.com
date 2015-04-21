"use strict";

var app = angular.module(
    'app', [
        'ngRoute',
        'ngResource',
        'app.main',
        'app.jsonService'
    ]
);

/**
 * Config
 */
app.config(function ($locationProvider, $routeProvider) {
    /*
     * Enabled HTML5 mode. Probably will not support
     * any browser especially < IE10
     */
    $locationProvider.html5Mode(true);

    /*
     * Routes for the mainApp
     */
    $routeProvider.when('/', {
        templateUrl: '/assets/app/modules/main/templates/main.html',
        controller: 'mainController'
    }).otherwise({redirectTo: '/404'});
});