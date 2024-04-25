import { Category } from "./category";

export interface Recipe{
    id?: number;
    title: string,
    description: string,
    image_url: string,
    category: Category,
    author: string,
    created_at: string,
    updated_at: string
}