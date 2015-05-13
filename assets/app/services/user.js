"use strict";

angular.module('app.main').factory('userService', function ($http, $q) {

    var userService = {};

    userService.googlePlusUserId = window.googlePlusUserId;
    userService.runkeeperUserId = window.runkeeperUserId;

    return userService;

});