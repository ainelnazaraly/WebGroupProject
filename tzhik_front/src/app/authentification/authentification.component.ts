import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-authentification',
  templateUrl: './authentification.component.html',
  styleUrl: './authentification.component.css'
})
export class AuthentificationComponent implements OnInit{
  
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
  }

  onSubmit(): void{
    this.authService.login(this.username, this.password).subscribe(
      () => {
        this.router.navigateByUrl('/home');
      },
      (error) => {
        // Handle login error
        console.error('Login error:', error);
      }
    );
  }
}
