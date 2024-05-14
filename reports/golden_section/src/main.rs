use tracing::info;


fn f(x: f64) -> f64 {
  x.powi(2) + 4.0 * x + 6.0
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
  tracing_subscriber::fmt().init();
  let min_p = golden_section_search(f, -4.0, 6.0);
  info!(min_p);
}