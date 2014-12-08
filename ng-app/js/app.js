
var localvore = angular.module("localvore", ['ngRoute', 'ngSanitize', 'ngMaterial']);

localvore.config(function ($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {controller: 'HomePageCtrl', templateUrl: '/tpl/homepage.html'})
    .when('/about', {controller: 'AboutCtrl', templateUrl: '/tpl/about.html'})
    .when('/places/', {controller: 'PlacesCtrl', templateUrl: '/tpl/places.html'})
    .when('/places/:categorySlug', {controller: 'PlacesCtrl', templateUrl: '/tpl/places.html'})
    .when('/place/:placeId', {controller: 'PlaceCtrl', templateUrl: '/tpl/place.html'})
    .otherwise({redirectTo: '/'});
    
  $locationProvider.html5Mode(true);
});


localvore.run(function ($rootScope, $location, $window) {
  $rootScope.set_title = function (title, post_fix) {
    if (post_fix) {
      $rootScope.title = 'Localvore.Guide: ' + title;
    }
    
    else {
      $rootScope.title = title + ' | Localvore.Guide';
    }
  };
  
  $rootScope.set_pushstate = function (obj) {
    console.log('Setting State:', obj, $rootScope.title, $location.path());
    $window.history.replaceState(obj, $rootScope.title, $location.path());
  };
  
  $rootScope.get_pushstate = function () {
    console.log('Getting State:', $window.history.state);
    return $window.history.state;
  };
});

localvore.filter('urlencode', function ($window) {
  return $window.encodeURIComponent;
});

function apply_updates ($scope) {
  if(!$scope.$$phase) {
    $scope.$apply();
  }
}
