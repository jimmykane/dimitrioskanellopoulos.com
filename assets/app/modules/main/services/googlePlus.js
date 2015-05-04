"use strict";

angular.module('app.main').factory('googlePlusService', function ($http, $q) {

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
        googlePlusService.profile = googlePlusService.getProfile || {};
        googlePlusService.getGooglePlusData(userId, 'profile');
        return googlePlusService.profile;
    };

    return googlePlusService;

});