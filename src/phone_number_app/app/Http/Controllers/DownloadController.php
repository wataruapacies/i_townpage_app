<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use App\Post;

class DownloadController extends Controller
{
    public function download($file)
    {
        $files = Storage::allFiles('public/python/result/');
        $files = str_replace('public/python/result/','',$files);
        $filePath = 'public/python/result/' . $file;
        $fileName = $file;
        $mimeType = Storage::mimeType($filePath);
        $headers = [['Content-Type' => $mimeType]];
        
        return Storage::download($filePath, $fileName, $headers);
    }
    public function delete($file)
    {
        $filePath = 'python/result/' . $file;
        Storage::disk('public')->delete($filePath);
        session()->flash('flash_message','ファイルを削除しました．');
        return redirect('top');
    }
    public function download_previous($file)
    {
        $files = Storage::allFiles('public/python/log/');
        $files = str_replace('public/python/log/','',$files);
        $filePath = 'public/python/log/' . $file;
        $fileName = $file;
        $mimeType = Storage::mimeType($filePath);
        $headers = [['Content-Type' => $mimeType]];
        
        return Storage::download($filePath, $fileName, $headers);
    }
    public function list()
    {
        $files = Storage::allFiles('public/python/result/');
        $files = str_replace('public/python/result/','',$files);
        return view('top', ['files' => $files]);
    }
    public function previous()
    {
        $files = Storage::allFiles('public/python/log/');
        $files = str_replace('public/python/log/','',$files);
        $posts=Post::all();
        return view('previous', compact('files','posts'));
    }
    public function scraping(Request $request)
    {
        return view('scraping',);
    }
}
