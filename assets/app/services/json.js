"use strict";

angular.module('app.jsonService', ['ngResource']).factory('jsonService', function($resource) {
    alert(1);
  return $resource('cats.json');
});