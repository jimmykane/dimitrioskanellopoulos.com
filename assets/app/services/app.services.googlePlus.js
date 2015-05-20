"use strict";

angular.module('app.services').factory('googlePlusService', function ($http, $q) {

    var googlePlusService = {};

    googlePlusService.getGooglePlusData = function (userId, call) {
        var deffered = $q.defer();
        $http.get('/apis/google+/' + userId + '/' + call)
            .success(function (data, status, headers, config) {
                if (status !== 200) {
                    deffered.resolve(data.status);
                    return;
                }
                // Extend with new data
                angular.extend(googlePlusService[call], data);
                deffered.resolve(status);
            })
            .error(function (data, status, headers, config) {
                deffered.reject(status);
                console.log(data, status, headers, config);
            });
        return deffered.promise;
    };

    googlePlusService.getProfile = function (userId) {
        googlePlusService.profile = googlePlusService.profile || {};
        googlePlusService.getGooglePlusData(userId, 'get_profile');
        return googlePlusService.profile;
    };

    googlePlusService.getProfileImageUrl = function(imageSize){
        if (!googlePlusService.profile.image){
            return;
        }
        return googlePlusService.profile.image.url.slice(0, -2) + imageSize;
    };

    googlePlusService.listActivities = function(userId){
        return googlePlusService.getGooglePlusData(userId, 'list_activities');
    };

    googlePlusService.isProfileReady = function (){
        return !angular.equals({}, $scope.profile);
    };

    return googlePlusService;

});