"use strict";

angular.module('app.jsonService', ['ngResource']).factory('JsonService', function($resource) {
    alert(1);
  return $resource('cats.json');
});