<ul>
    @foreach ($users as $user)
        <li>{{ $user->name }} ({{ $user->email }})</li>
    @endforeach
</ul>

@forelse ($items as $item)
    <li>{{ $item }}</li>
@empty
    <p>No items found.</p>
@endforelse
