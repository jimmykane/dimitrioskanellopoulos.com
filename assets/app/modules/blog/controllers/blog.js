"use strict";

angular.module('app.blog').controller('blogController', function ($scope, userService, googlePlusService) {
    $scope.googlePlusActivities = googlePlusService.listActivities(userService.googlePlusUserId);
});