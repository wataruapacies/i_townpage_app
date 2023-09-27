<?php
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\DownloadController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('start');
});
Route::group(['middleware' => 'auth'], function () {
    Route::get('/top/', [DownloadController::class, 'list']);
    Route::get('/previous/', [DownloadController::class, 'previous']);
    Route::get('/scraping/', [DownloadController::class, 'scraping']);
    Route::get('/after/', function (){
        return view('after');
    });
    
    Route::get('/download/{file}', 'DownloadController@download')->name('file.download');
    Route::get('/delete/{file}', 'DownloadController@delete')->name('file.delete');
    Route::get('/download_previous/{file}', 'DownloadController@download_previous')->name('file.download_previous');
    Route::post('/previous', 'PostController@post');
    Route::post('/previous/destroy/{id}', 'PostController@destroy')->name('post.destroy');
});


Auth::routes(['register' => false]);

Route::get('/home', 'HomeController@index')->name('home');
