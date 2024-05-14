use nalgebra::{Matrix2, Vector2};
use tracing::info;

fn f(p: &Vector2<f64>) -> f64 {
    3.0 * (p.x.powi(2)) + p.y.powi(2) - p.x * p.y + p.x
}

fn grad<F: Fn(&Vector2<f64>) -> f64>(f: F, p: &Vector2<f64>) -> Vector2<f64> {
    let h = 1e-6;

    let dx = Vector2::<f64>::new(h, 0.0);
    let dy = Vector2::<f64>::new(0.0, h);

    Vector2::new(
        (f(&(p + &dx)) - f(&(p - &dx))) / (2.0 * h),
        (f(&(p + &dy)) - f(&(p - &dy))) / (2.0 * h),
    )
}

fn main() {
    tracing_subscriber::fmt().init();

    let hesse = Matrix2::<f64>::new(2.0 / 27.0, 1.0 / 27.0, 1.0 / 27.0, 14.0 / 27.0);

    let m = 50;
    let eps1 = 0.1;
    let eps2 = 0.15;

    let x0 = Vector2::<f64>::new(1.5, 1.5);

    let mut x = vec![x0];

    let mut k = 0;
    let mut first_check = false;
    while k < m {
      let x_prev = x.last().cloned().unwrap();
      let gk = grad(f, &x_prev);
      let d_k = hesse * gk * -1.0;
      let x_next = x_prev + d_k;
      x.push(x_next.clone());

      if grad(f, &x_next).magnitude() < eps1 {
        break;
      }
      if k > 1 && (x_next - x_prev).magnitude() < eps2 {
        if first_check {
          break;
        }
        else {
          first_check = true;
        }
      }
      else {
        first_check = false;
      }
      k += 1;
    }

    let target_x = x.last().unwrap();
    let value_at_target = f(target_x);
    info!(%target_x);
    info!(%value_at_target);
}
