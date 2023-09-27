<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use App\Post;

class PostController extends Controller
{
    public function post(Request $request)
    {
        $inputs=request()->validate([
            'what'=>'required|max:255',
            'where'=>'required|max:255',
        ],
        [
            'what.required' => 'キーワードは必須です',
            'where.required' => 'エリア・駅は必須です'
        ]);
        $post=new Post();
        $post->what=$request->what;
        $post->where=$request->where;
        $post->save();
        $files = Storage::allFiles('public/python/log/');
        $files = str_replace('public/python/log/','',$files);
        $posts=Post::all();
        session()->flash('flash_message','スクレイピング予約リストに保存しました');
        return view('previous', compact('files','posts'));
    }
    public function destroy($id)
    {
        $post = Post::find($id);
        $post->delete();
        session()->flash('flash_message','スクレイピング予約を取り消しました');
        return redirect('previous');
    }
}
