@extends('layouts.app')

@section('content')
    <h1>スクレイピング予約</h1>
    <p class="teaching">※
    <a href="https://itp.ne.jp/">iタウンページ</a>
    のスクレイピングをおこないます</p>
        @foreach ($errors->all() as $error)
        <div class="warning-mess alert alert-warning" role="alert">
        {{ $error }}
</div>
        @endforeach

    <div class="input_zone">
    <form action="/previous" method="post">
    @csrf
    <div class="form-group">
    <input name="what" class="form-control" placeholder="キーワードを入力">
    </div>
    <div class="form-group">
    <input name="where" class="form-control" placeholder="エリア・駅">
    </div>
    <button type="submit" class="btn btn-primary">追加</button>
    </form>
    </div>
@endsection