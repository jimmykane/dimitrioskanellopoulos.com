"use strict";

angular.module('app.services').factory('userService', function ($http, $q) {

    var userService = {};

    userService.googlePlusUserId = window.googlePlusUserId;
    userService.runkeeperUserId = window.runkeeperUserId;

    return userService;

});