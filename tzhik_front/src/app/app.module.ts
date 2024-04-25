import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthentificationComponent } from './authentification/authentification.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { LikesComponent } from './likes/likes.component';
import { RecipeListComponent } from './recipe-list/recipe-list.component';
import { CategoryComponent } from './category/category.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    AuthentificationComponent,
    LoginComponent,
    HomeComponent,
    LikesComponent,
    RecipeListComponent,
    CategoryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
