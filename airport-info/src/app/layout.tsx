import NavBar from "@/components/NavBar";
//Why am I getting an error for above? This was pulled straight from the provided files no changes made. 
import Grid from '@mui/material/Unstable_Grid2';

import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Airport Information",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
      <NavBar />
      <Grid container alignItems={"center"} justifyContent={"center"}>
          <Grid xs={11}>
              <br />
          </Grid>
          <Grid xs={11}>
              {children}
          </Grid>
      </Grid>
      </body>
    </html>
);
}