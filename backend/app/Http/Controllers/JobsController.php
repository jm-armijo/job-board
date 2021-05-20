<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class JobsController extends Controller
{
    public function getAll()
    {
        $results = DB::select("SELECT id, title, location, date FROM jobs");
        return $results;
    }
}
