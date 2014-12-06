var CAT_SLUGS = {}
CAT_SLUGS['farmers-markets'] = 'Farmers Markets';

localvore.controller("PlacesCtrl", function ($scope, $routeParams) {
  $scope.location = {};
  $scope.cat = $routeParams.categorySlug;
  
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
    console.log(position);
  };
  
  $scope.get_location();
});
