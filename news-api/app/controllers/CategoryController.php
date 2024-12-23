<?php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;

class CategoryController extends Controller
{
    // Fetch all categories
    public function index()
    {
        $categories = Category::all();
        return response()->json($categories);
    }

    // Fetch a single category by ID
    public function show($id)
    {
        $category = Category::find($id);

        if (!$category) {
            return response()->json(['error' => 'Category not found'], 404);
        }

        return response()->json($category);
    }

    // Create a new category
    public function store(Request $request)
    {
        // Validate incoming request
        $request->validate([
            'name' => 'required|string|max:255',
        ]);

        // Create a new category
        $category = Category::create([
            'name' => $request->input('name'),
        ]);

        return response()->json($category, 201);
    }

    // Update an existing category
    public function update(Request $request, $id)
    {
        // Find category by ID
        $category = Category::find($id);

        if (!$category) {
            return response()->json(['error' => 'Category not found'], 404);
        }

        // Validate incoming request
        $request->validate([
            'name' => 'required|string|max:255',
        ]);

        // Update category name
        $category->name = $request->input('name');
        $category->save();

        return response()->json($category);
    }

    // Delete a category
    public function destroy($id)
    {
        // Find category by ID
        $category = Category::find($id);

        if (!$category) {
            return response()->json(['erro
