var CAT_SLUGS = {};
CAT_SLUGS['farmers-markets'] = 'Farmers Markets';

localvore.controller("PlacesCtrl", function ($scope, $routeParams, $http) {
  $scope.location = {};
  $scope.cat = $routeParams.categorySlug;
  $scope.places = [];
  $scope.loading = false;
  
  if ($scope.cat) {
    $scope.set_title(CAT_SLUGS[$scope.cat]);
  }
  
  else {
    $scope.set_title('Listings');
  }
  
  $scope.get_location = function () {
    if (localStorage.search_location) {
      $scope.location = JSON.parse(localStorage.search_location);
    }
    
    else {
      navigator.geolocation.getCurrentPosition($scope.set_location)
    }
  };
  
  $scope.set_location = function (position) {
    $scope.location.lat = position.coords.latitude;
    $scope.location.lon = position.coords.longitude;
    
    $scope.location.address = '';
    $scope.location.city = '';
    $scope.location.state = '';
    
    apply_updates($scope);
    $scope.get_places();
  };
  
  $scope.get_places = function () {
    $scope.loading = true;
    
    var url = '/backend/api/places.json?lat=' + $scope.location.lat + '&lon=' + $scope.location.lon;
    
    $http.get(url)
    .success(function (data) {
      $scope.places = data;
      $scope.loading = false;
    });
  };
  
  $scope.get_location();
});
