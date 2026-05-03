@if (count($records) === 1)
    I have one record!
@elseif (count($records) > 1)
    I have multiple records!
@else
    I don't have any records!
@endif

@auth
    // The user is authenticated...
@endauth

@guest
    // The user is not authenticated...
@endguest
