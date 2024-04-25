import { NgModule } from '@angular/core';
import { LoginComponent } from './login/login.component';
import { AuthentificationComponent } from './authentification/authentification.component';
import { HomeComponent } from './home/home.component';
import { RouterModule, Routes } from '@angular/router';
import { LikesComponent } from './likes/likes.component';

const routes: Routes = [
  { path: '', component: LoginComponent},
  { path: 'authentification', component: AuthentificationComponent},
  { path: 'home', component: HomeComponent},
  { path: 'likes', component: LikesComponent}
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
