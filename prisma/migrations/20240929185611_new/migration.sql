-- CreateTable
CREATE TABLE "Fact" (
    "Fact_id" TEXT NOT NULL,
    "Fact" TEXT NOT NULL,
    "num_views" INTEGER NOT NULL,

    CONSTRAINT "Fact_pkey" PRIMARY KEY ("Fact_id")
);
