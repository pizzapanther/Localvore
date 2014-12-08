var CAT_SLUGS = {};
CAT_SLUGS['farmers-markets'] = 'Farmers Markets';
CAT_SLUGS['stores'] = 'Stores';
CAT_SLUGS['restaurants'] = 'Restaurants';

localvore.controller("PlacesCtrl", function ($scope, $routeParams, $http) {
  $scope.location = {};
  $scope.form = {};
  $scope.cat = $routeParams.categorySlug;
  $scope.places = [];
  $scope.loading = false;
  $scope.show_form = false;
  $scope.cats = CAT_SLUGS;
  
  $scope.geocoder = new google.maps.Geocoder();
  
  if ($scope.cat) {
    $scope.set_title(CAT_SLUGS[$scope.cat]);
    $scope.page_title = CAT_SLUGS[$scope.cat];
  }
  
  else {
    $scope.set_title('All Listings');
    $scope.page_title = 'All Listings';
  }
  
  $scope.hide_me = function (slug) {
    return slug === $scope.cat;
  };
  
  $scope.reset_location = function () {
    navigator.geolocation.getCurrentPosition($scope.set_location)
  };
  
  $scope.get_location = function () {
    if (localStorage.search_location) {
      $scope.location = JSON.parse(localStorage.search_location);
      angular.copy($scope.location, $scope.form);
      $scope.get_places();
    }
    
    else {
      navigator.geolocation.getCurrentPosition($scope.set_location)
    }
  };
  
  $scope.address_entered =function () {
    return $scope.location.address || $scope.location.city || $scope.location.state;
  };
  
  $scope.set_location = function (position) {
    $scope.location.lat = position.coords.latitude;
    $scope.location.lon = position.coords.longitude;
    
    $scope.location.address = '';
    $scope.location.city = '';
    $scope.location.state = '';
    
    localStorage.setItem("search_location", JSON.stringify($scope.location));
    
    apply_updates($scope);
    $scope.get_places(true);
  };
  
  $scope.get_places = function (skip_state) {
    var state = $scope.get_pushstate();
    
    if (state && !skip_state) {
      $scope.places = state.data;
      $scope.location = state.location
    }
    
    else {
      if ($scope.location.lat) {
        $scope.loading = true;
        $scope.places = [];
        
        var url = '/backend/api/places.json?lat=' + $scope.location.lat + '&lon=' + $scope.location.lon;
        if ($scope.cat) {
          url += '&placetype=' + $scope.cat;
        }
        
        $http.get(url)
        .success(function (data) {
          $scope.places = data;
          $scope.loading = false;
          
          $scope.set_pushstate({data: data, location: $scope.location});
        });
      }
      
      else {
        $scope.get_location();
      }
    }
  };
  
  $scope.display_form = function () {
    $scope.show_form = true;
  };
  
  $scope.find_address = function () {
    var address = '';
    if ($scope.form.address) {
      address += $scope.form.address;
    }
    
    if ($scope.form.city) {
      if (address !== '') {
        address += ' ';
      }
      
      address += $scope.form.city;
    }
    
    if ($scope.form.state) {
      if (address !== '') {
        address += ' ';
      }
      
      address += $scope.form.state;
    }
    
    $scope.geocoder.geocode( {address: address}, function (results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        angular.copy($scope.form, $scope.location);
        
        $scope.location.lat = results[0].geometry.location.lat();
        $scope.location.lon = results[0].geometry.location.lng();
        
        localStorage.setItem("search_location", JSON.stringify($scope.location));
        $scope.get_places(true);
      }
      
      else {
        alert('Could not find location entered');
      }
    });
  };
  
  $scope.get_places();
});

localvore.controller("PlaceCtrl", function ($scope, $routeParams, $http, $timeout) {
  $scope.loading = false;
  $scope.place = null;
  $scope.id = $routeParams.placeId;
  $scope.set_title('Place ' + $scope.id);
  
  $scope.load_place = function () {
    $scope.loading = true;
    $scope.place = null;
    $scope.map = null;
    
    var state = $scope.get_pushstate();
    if (state) {
      $scope.place = state;
      $scope.loading = false;
      $scope.set_title($scope.place.name);
    }
    
    else {
      var url = '/backend/api/' + $scope.id + '.json';
      
      $http.get(url)
      .success(function (data) {
        $scope.place = data;
        $scope.loading = false;
        $scope.set_title($scope.place.name);
        
        $scope.set_pushstate(data);
      });
    }
  };
  
  $scope.load_place();
});

