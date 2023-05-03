use reqwest::blocking::Client;
use std::env;
use std::fs::File;
use std::io::copy;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        println!("Usage: {} <url>", args[0]);
        return Ok(());
    }

    let url = &args[1];
    let filename = &args[2];

    let mut resp = Client::new().get(url).send()?;
    let mut out_file = File::create(filename)?;

    copy(&mut resp, &mut out_file)?;

    Ok(())
}
