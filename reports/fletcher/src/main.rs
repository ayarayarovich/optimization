use nalgebra::Vector2;
use tracing::info;

fn f(p: &Vector2<f64>) -> f64 {
    3.0 * p.x.powi(2) + p.y.powi(2) - p.x * p.y + p.x
}

fn gradf(p: &Vector2<f64>) -> Vector2<f64> {
    Vector2::new(6.0 * p.x - p.y + 1.0, 2.0 * p.y - p.x)
}

fn golden_section_search<F: Fn(f64) -> f64>(f: F, mut a: f64, mut b: f64) -> f64 {
    let tol = 1e-5;
    let gr = (1.0f64 + 5.0f64.sqrt()) / 2.0f64;
    let mut c = b - (b - a) / gr;
    let mut d = a + (b - a) / gr;
    while (c - d).abs() > tol {
        if f(c) < f(d) {
            b = d;
        } else {
            a = c;
        }
        c = b - (b - a) / gr;
        d = a + (b - a) / gr;
    }
    return (b + a) / 2.0;
}

fn main() {
    tracing_subscriber::fmt().with_target(false).init();

    let x0 = Vector2::<f64>::new(1.1, 1.1);

    let mut x = x0;
    let tol = 1e-5;
    let m = 50;

    let mut grad = gradf(&x0);
    let mut p: Vector2<f64> = -grad;

    for k in 0..m {
        let alpha = golden_section_search(|alpha| f(&(&x + alpha * &p)), 0.0, 1.0);

        let next_x = x + alpha * p;
        let next_grad = gradf(&next_x);

        if next_grad.magnitude() < tol {
            info!("Метод сошелся на итерации {k}");
            break;
        }

        info!(
            "Итерация {k}: x = {next_x}, f(x) = {}, alpha = {alpha}",
            f(&next_x)
        );

        let beta = next_grad.dot(&next_grad) / grad.dot(&grad);

        p = -next_grad + beta * p;
        x = next_x;
        grad = next_grad;
    }

    info!("Результат X = {x}");
    info!("Значение в точке: {}", f(&x));
}
